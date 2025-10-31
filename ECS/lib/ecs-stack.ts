import * as cdk from 'aws-cdk-lib';
import { BastionHostLinux, InstanceType, SecurityGroup, SubnetType, Vpc } from 'aws-cdk-lib/aws-ec2';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { DatabaseSecret, ParameterGroup } from 'aws-cdk-lib/aws-rds';
import { Construct } from 'constructs';
import path from 'path';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class EcsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    const vpc = new Vpc(this, "auroroa",{
      maxAzs: 2
    })


        // A security group with no inbound (Session Manager doesn't need it)
    const sg = new SecurityGroup(this, 'BastionSG', {
      vpc,
      allowAllOutbound: true,
      description: 'Bastion host SG for SSM access (no inbound rules)',
    });

    const bastion = new BastionHostLinux(this, "bastionHost", {
      instanceName: "AdminClient1",
      vpc,
      subnetSelection: { subnetType: SubnetType.PUBLIC },
      securityGroup: sg,
      requireImdsv2: true,
      instanceType: cdk.aws_ec2.InstanceType.of(cdk.aws_ec2.InstanceClass.T3,cdk.aws_ec2.InstanceSize.MEDIUM)
    })


        // Attach the SSM role to the instance
    bastion.instance.addToRolePolicy(
      new PolicyStatement({
        actions: [
          "secretsmanager:ListSecrets",
          "secretsmanager:*",
          "elasticloadbalancing:DescribeLoadBalancers",
          "ssm:GetParameter", "ssm:PutParameter",
          'ssmmessages:*',
          'ssm:UpdateInstanceInformation',
          'ec2messages:*',
        ],
        resources: ['*'],
      })
    );

    new NodejsFunction(this, "test-postgtes", {
      entry: path.join(__dirname, "../handlers/basic/index.ts"),
      handler: "index.handler",
      vpc,
      bundling: {
        // Tell esbuild to treat .pem files as text and inline them
        loader: { ".pem": "text" },
        // optional: keep pg external if you prefer
        externalModules: [], 
      },
    })
  }
}


/*

aws secretsmanager list-secrets --max-results 20
aws secretsmanager get-secret-value --region ap-south-1 --secret-id "arn:aws:secretsmanager:ap-south-1:339713054130:secret:rds!cluster-02dab5ce-d0a6-4645-b02a-a2a3570c5059-9hb6MX" -query SecretString --output text


aws secretsmanager get-secret-value \
  --region "ap-south-1" \
  --secret-id "arn:aws:secretsmanager:ap-south-1:339713054130:secret:rds!cluster-02dab5ce-d0a6-4645-b02a-a2a3570c5059-9hb6MX" \
  --output text



  SECRET_JSON=$(aws secretsmanager get-secret-value \
  --region "ap-south-1" \
  --secret-id "arn:aws:secretsmanager:ap-south-1:339713054130:secret:rds!cluster-02dab5ce-d0a6-4645-b02a-a2a3570c5059-9hb6MX" \
  --query SecretString \
  --output text)
{"username":"postgres","password":"CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug"}

HOST=$(echo "$SECRET_JSON" | jq -r '.host')
PORT=$(echo "$SECRET_JSON" | jq -r '.port')
USER=$(echo "$SECRET_JSON" | jq -r '.username')
PASS=$(echo "$SECRET_JSON" | jq -r '.password')
DB=$(echo "$SECRET_JSON"   | jq -r '.dbname')


PGPASSWORD='<password>' psql \
  -h <host> \
  -p 5432 \
  -U <username> \
  -d <database> \
  -v sslmode=require

  PGPASSWORD="CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug" psql -h database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com -U postgres -d postgres -p 5432 -f root/vishal/load_seed_data.sql

  psql -h database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com -U postgres -d postgres -p 5432 -f /root/vishal/schema.sql


  load_seed_data.sql

  \COPY symbol(ticker,volume,open,close,high,low) FROM 'root/vishal/stocks.csv' DELIMITER ',' CSV HEADER;
  \COPY customer(first_name,last_name) FROM 'root/vishal/customers.csv' DELIMITER ',' CSV HEADER;
  \dt. 

  PGPASSWORD="CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug" psql -h database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com -U postgres -d postgres -p 5432 \
       -c "\COPY symbol(ticker,volume,open,close,high,low) FROM '/root/vishal/stocks.csv' DELIMITER ',' CSV HEADER;" \
     -c "\COPY customer(first_name,last_name) FROM '/root/vishal/customers.csv' DELIMITER ',' CSV HEADER;" \
     -c "\dt"


*/