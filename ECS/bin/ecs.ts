#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EcsStack } from '../lib/ecs-stack';
import { CloudfrontAPIStack } from '../lib/Stacks/CloudFrontStacks/cloudfront-api.stack';


const app = new cdk.App();

new CloudfrontAPIStack(app, 'CloudfrontAPIStack', {
   env: { account: '339713054130', region: 'ap-south-1' },
});
// new EcsStack(app, 'AuroraEcsStack1', {
//    env: { account: '339713054130', region: 'ap-south-1' },
// });