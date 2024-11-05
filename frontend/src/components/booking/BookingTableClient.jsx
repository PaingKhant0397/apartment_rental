import {
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Button,
  Pagination,
  Paper,
  Select,
  MenuItem,
} from '@mui/material'
import { useEffect } from 'react'

function BookingTableClient({
  bookings,
  onEdit,
  onDelete,
  totalCount,
  currentPage,
  setCurrentPage,
  limit,
  bookingStatuses,
  statusesLoading,
}) {
  const totalPages = Math.ceil(totalCount / limit)

  const handlePageChange = (event, newPage) => {
    setCurrentPage(newPage)
  }

  return (
    <div className='p-4 w-full'>
      <Paper elevation={3} className='p-4'>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell align='center'>Apartment</TableCell>
              <TableCell align='center'>Room Type</TableCell>
              <TableCell align='center'>Price</TableCell>
              <TableCell align='center'>Deposit</TableCell>
              <TableCell align='center'>Date</TableCell>

              <TableCell align='center'>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {bookings.map(booking => (
              <TableRow key={booking.booking_id} hover>
                {/* <TableCell align='center'>{booking.user.user_email}</TableCell> */}
                <TableCell align='center'>
                  {booking.room_type.apartment_name}
                </TableCell>
                <TableCell align='center'>
                  {booking.room_type.room_type.room_type_name}
                </TableCell>
                <TableCell align='center'>
                  {booking.room_type.available_room_type_price}
                </TableCell>
                <TableCell align='center'>
                  {booking.room_type.available_room_type_deposit_amount}
                </TableCell>
                <TableCell align='center'>{booking.booking_date}</TableCell>

                <TableCell align='center'>
                  {booking.status.booking_status_name}
                </TableCell>

                {/* <TableCell align='center'>
                  <Button
                    variant='outlined'
                    color='error'
                    onClick={() => onDelete(booking.booking_id)}
                  >
                    Delete
                  </Button>
                </TableCell> */}
              </TableRow>
            ))}
          </TableBody>
        </Table>
        {/* Pagination Controls */}
        <div className='flex justify-center mt-4'>
          <Pagination
            count={totalPages}
            page={currentPage}
            onChange={handlePageChange}
            color='primary'
            shape='rounded'
          />
        </div>
      </Paper>
    </div>
  )
}

export default BookingTableClient
