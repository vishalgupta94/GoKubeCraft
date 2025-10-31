import * as cdk from 'aws-cdk-lib';
import { CfnRestApi, EndpointType, Integration, LambdaIntegration, RestApi } from 'aws-cdk-lib/aws-apigateway';
import { AttributeType, TableV2 } from 'aws-cdk-lib/aws-dynamodb';
import { HttpMethod } from 'aws-cdk-lib/aws-events';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';
import path from 'path';


export class CloudfrontAPIStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    
    const table = new TableV2(this,"table", {
        partitionKey: {
            name: "PK",
            type: AttributeType.STRING
        },
        sortKey:{
            name: "SK",
            type: AttributeType.STRING
        },
    })

    table.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY)

    const api = new RestApi(this, "CloudfrontAPI",{
        endpointTypes: [EndpointType.REGIONAL],
    })
    
    api.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY)

    const lambda = new NodejsFunction(this, "lambda",{
      entry: path.join(__dirname, "../../../handlers/cloudfrontStacks/basic-lambda/index.ts") 
    })

    lambda.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY)
    
    const getResource = api.root.addResource("getItems")

    const integration =new LambdaIntegration(lambda)

    getResource.addMethod(HttpMethod.GET, integration)

    const postResource = api.root.addResource("postItemsItems")

    postResource.addMethod(HttpMethod.POST, integration)
    
  }
}
