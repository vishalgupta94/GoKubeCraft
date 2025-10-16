import { Pool } from "pg";


// Create a connection pool
export const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'postgres',
  password: 'mysecretpassword',
  port: 5432, // default PostgreSQL port
});
