import * as cdk from "aws-cdk-lib";
import {
  CfnRestApi,
  EndpointType,
  Integration,
  LambdaIntegration,
  RestApi,
} from "aws-cdk-lib/aws-apigateway";
import {
  CloudFrontWebDistribution,
  Distribution,
  DistributionProps,
  S3OriginAccessControl,
} from "aws-cdk-lib/aws-cloudfront";
import { S3BucketOrigin } from "aws-cdk-lib/aws-cloudfront-origins";
import { AttributeType, TableV2 } from "aws-cdk-lib/aws-dynamodb";
import { HttpMethod } from "aws-cdk-lib/aws-events";
import { Tracing } from "aws-cdk-lib/aws-lambda";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Bucket } from "aws-cdk-lib/aws-s3";
import { Construct } from "constructs";
import path from "path";

export class CloudfrontAPIStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new TableV2(this, "table", {
      partitionKey: {
        name: "PK",
        type: AttributeType.STRING,
      },
      sortKey: {
        name: "SK",
        type: AttributeType.STRING,
      },
    });

    table.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);

    const api = new RestApi(this, "CloudfrontAPI", {
      endpointTypes: [EndpointType.REGIONAL],
      deployOptions: {
        tracingEnabled: true,
        // <snip>
      },
    });

    api.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);

    const lambda = new NodejsFunction(this, "lambda", {
      entry: path.join(
        __dirname,
        "../../../handlers/cloudfrontStacks/basic-lambda/index.ts"
      ),
      environment: {
        ITEM_TABLE: table.tableName,
      },
      tracing: Tracing.PASS_THROUGH,
    });

    table.grantFullAccess(lambda);

    lambda.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);

    const getResource = api.root.addResource("getItems");

    const integration = new LambdaIntegration(lambda);

    getResource.addMethod(HttpMethod.GET, integration);

    const postResource = api.root.addResource("postItemsItems");
    const integrationPOST = new LambdaIntegration(lambda, {});

    postResource.addMethod(HttpMethod.POST, integrationPOST, {});

    postResource.addCorsPreflight({
      allowOrigins: ["*"],
    });

    const bucket = new Bucket(this, "s3Bucket", {});

    const origin = S3BucketOrigin.withOriginAccessControl(bucket, {
      originAccessControl: new S3OriginAccessControl(this, "oac", {
        originAccessControlName: "oac",
      }),
    });

    const cloudfront = new Distribution(this, "cdn", {
      defaultBehavior: {
        origin: origin,
      },
    } as DistributionProps);
  }
}
