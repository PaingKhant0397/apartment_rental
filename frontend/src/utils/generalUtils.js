export const getTodayDateString = () => {
  const today = new Date()
  const day = String(today.getDate()).padStart(2, '0')
  const month = String(today.getMonth() + 1).padStart(2, '0') // Months are 0-based
  const year = today.getFullYear()

  return `${day}/${month}/${year}`
}

export const generateInvoiceHTML = invoiceData => {
  const {
    invoice_id,
    rental,
    status,
    water_bill,
    electricity_bill,
    total_amount,
    issued_date,
    due_date,
  } = invoiceData

  const {
    rental_id,
    room,
    user,
    rental_status,
    rental_start_date,
    rental_end_date,
  } = rental

  const {
    apartment_name,
    room_type: { room_type_name },
    available_room_type_price,
    available_room_type_deposit_amount,
    room_no,
    room_size,
    room_floor_no,
  } = room.available_room_type

  return `
    <html>
      <head>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
          }
          .invoice-container {
            background: white;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: auto;
          }
          h1, h2, h3 {
            color: #333;
          }
          .header {
            text-align: center;
            margin-bottom: 20px;
          }
          .details, .totals {
            margin-bottom: 20px;
          }
          .details div, .totals div {
            margin-bottom: 10px;
          }
          .footer {
            margin-top: 20px;
            font-size: 14px;
            color: #888;
          }
          .table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
          }
          .table th, .table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
          }
          .table th {
            background-color: #f2f2f2;
          }
        </style>
      </head>
      <body>
        <div class="invoice-container">
          <div class="header">
            <h1>Invoice</h1>
            <h2>Invoice #${invoice_id}</h2>
          </div>

          <div class="details">
            <h3>Rental Details:</h3>
            <div><strong>Rental ID:</strong> ${rental_id}</div>
            <div><strong>Apartment:</strong> ${apartment_name}</div>
            <div><strong>Room Type:</strong> ${room_type_name}</div>
            <div><strong>Room Number:</strong> ${room_no}</div>
            <div><strong>Room Size:</strong> ${room_size}</div>
            <div><strong>Floor Number:</strong> ${room_floor_no}</div>
            <div><strong>User Name:</strong> ${user.user_name}</div>
            <div><strong>User Email:</strong> ${user.user_email}</div>
            <div><strong>Rental Status:</strong> ${rental_status.rental_status_name}</div>
           
          </div>

          <h3>Billing Details:</h3>
          <table class="table">
            <tr>
              <th>Room Pricel</th>
              <th>Water Bill</th>
              <th>Electricity Bill</th>
              <th>Total Amount</th>
            </tr>
            <tr>
              <td>$${available_room_type_price}</td>
              <td>$${water_bill.toFixed(2)}</td>
              <td>$${electricity_bill.toFixed(2)}</td>
              <td>$${total_amount.toFixed(2)}</td>
            </tr>
          </table>

          <div class="totals">
            <div><strong>Invoice Status:</strong> ${status.invoice_status_name}</div>
            <div><strong>Issued Date:</strong> ${issued_date}</div>
            <div><strong>Due Date:</strong> ${due_date}</div>
          </div>

          <div class="footer">
            <p>Thank you for your business!</p>
          </div>
        </div>
      </body>
    </html>
  `
}
