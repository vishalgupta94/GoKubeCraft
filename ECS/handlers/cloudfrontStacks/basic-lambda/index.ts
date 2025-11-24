import {
  APIGatewayEvent,
  APIGatewayProxyResultV2,
  APIGatewayRequestIAMAuthorizerV2WithContextHandler,
} from "aws-lambda";
import { marshall, unmarshall } from "@aws-sdk/util-dynamodb";
import {
  DeleteItemCommand,
  DynamoDBClient,
  GetItemCommand,
  GetItemCommandInput,
  PutItemCommand,
  PutItemCommandInput,
  QueryCommand,
} from "@aws-sdk/client-dynamodb";
import { captureAWSv3Client } from 'aws-xray-sdk';
const docClientWithoutXRAY = new DynamoDBClient({
  region: "ap-south-1",
});

const docClient = captureAWSv3Client(docClientWithoutXRAY)
export const handler = async (
  event: APIGatewayEvent
): Promise<APIGatewayProxyResultV2> => {
  console.log("event", event, event.httpMethod);

  if (event.httpMethod == "GET") {
    console.log("GET");
    const PK = event.queryStringParameters?.PK
    const SK = event.queryStringParameters?.SK
    const input: GetItemCommandInput = {
      TableName: process.env.ITEM_TABLE,
      Key: marshall({
          PK,
          SK,
        })
    };
    const putItemCommand = new GetItemCommand(input);
    const data = await docClient.send(putItemCommand);
    
    const item = data.Item

    

    return {
      statusCode: 200,
      headers: {
        "Content-Type": "application/json",
      },
      body: item ? JSON.stringify(unmarshall(item)): JSON.stringify({})
    };
  }

  if (event.httpMethod == "POST") {
    console.log("event.body", event.body);
    const eventBody = event.body;
    if (eventBody) {
      const body = JSON.parse(eventBody);
      const PK = body.PK;
      const SK = body.SK;
      const input: PutItemCommandInput = {
        Item: marshall({
          PK,
          SK,
        }),
        TableName: process.env.ITEM_TABLE,
      };
      const putItemCommand = new PutItemCommand(input);
      await docClient.send(putItemCommand);
      return {
        statusCode: 200,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          key: "POST",
          body: event.body,
          PK,
          SK,
        }),
      };
    } else {
      return {
        statusCode: 400,
        headers: {
          "Content-Type": "application/json",
        },
      };
    }
  }

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      key: "DEFAULT",
    }),
  };
};

// PGPASSWORD="CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug" psql -h database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com -U postgres -d postgres -p 5432
