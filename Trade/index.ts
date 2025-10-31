import { pool } from "./db.ts";


async function getActivities() {
  try {
    const result = await pool.query('SELECT * FROM symbol;'); //symbol //activity
    console.log(result.rows);
  } catch (err) {
    console.error('Error querying the database:', err);
  } finally {
    await pool.end(); // Close connection
  }
}

async function executeTrade() {
    const request = {
        "request_id": "req-10001",
        "customer_id": 1,
        "ticker": "CAT",
        "transaction_type": "buy",
        "share_count": 5,
        "current_price": 220.16
    }

    const customer = await pool.query(`SELECT * FROM customer where id = ${request.customer_id};`); //symbol //activity
    console.log(customer.rows);

    const stocks = await pool.query(`SELECT * FROM symbol where ticker = $1;`, [request.ticker]); //symbol //activity
    console.log(stocks.rows);   
    
    if (customer.rows.length > 0 && stocks.rows.length > 0) {
         const activity = await pool.query(`
                INSERT INTO activity (
                    request_id, customer_id, symbol_ticker, type, current_price, share_count, status
                )
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                RETURNING *;
                `, [
                    request.request_id,
                    customer.rows[0].id,
                    stocks.rows[0].id!,
                    'buy', 
                    220.16,       
                    5,    
                    'submitted'                    
                ]); //symbol //activity

         const result = await pool.query('SELECT * FROM activity;'); //symbol //activity
         console.log(result.rows);
        
    }
}

executeTrade()