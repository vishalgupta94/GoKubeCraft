import {
  APIGatewayEvent,
  APIGatewayProxyResultV2,
  APIGatewayRequestIAMAuthorizerV2WithContextHandler,
} from "aws-lambda";

export const handler = async(event: APIGatewayEvent): Promise<APIGatewayProxyResultV2> => {
  console.log("event", event, event.httpMethod);

  if (event.httpMethod == "GET") {
    console.log("GET",);
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        key: "GET",
      }),
    };
  }

  if (event.httpMethod == "POST") {
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        key: "POST",
      }),
    };
  }

  return {
    statusCode: 200,
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      key: "DEFAULT",
    }),
  };
};

// PGPASSWORD="CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug" psql -h database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com -U postgres -d postgres -p 5432
