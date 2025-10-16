import { pool } from "./db";


async function getActivities() {
  try {
    const result = await pool.query('SELECT * FROM customer;');
    console.log(result.rows);
  } catch (err) {
    console.error('Error querying the database:', err);
  } finally {
    await pool.end(); // Close connection
  }
}

getActivities();