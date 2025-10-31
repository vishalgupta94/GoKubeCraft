
import { Pool } from "pg";
import path from "path";
const rdsCa = path.join(__dirname, "ap-south-1-bundle.pem");
// import rdsCa from "./ap-south-1-bundle.pem";
// Create a connection pool



export const handler = async(event : any ) => {
//  const rdsCa = readFileSync("./ap-south-1-bundle.pem", "utf8");
 const pool = new Pool({
  user: 'postgres',
  host: 'database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com',
  database: 'postgres',
  password: "CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug",
  port: 5432, // default PostgreSQL port
    ssl: {
    ca: rdsCa,            // trust only Amazon RDS CA
    rejectUnauthorized: true,
  },
});
    console.log("event",event)
   try {
   
    const result = await pool.query('SELECT * FROM symbol;'); //symbol //activity

    console.log("result",result)
    console.log(result.rows);
  } catch (err) {

    console.log("err",err)
    console.error('Error querying the database:', err);
  } finally {
    await pool.end(); // Close connection
  }
}

// PGPASSWORD="CkIXm3*jIwBRm8ZGmv:Kwqj2e1ug" psql -h database-1-instance-1.chc4um4a6h90.ap-south-1.rds.amazonaws.com -U postgres -d postgres -p 5432