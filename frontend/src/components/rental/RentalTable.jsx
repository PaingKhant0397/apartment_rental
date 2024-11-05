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

function RentalTable({
  rentals,
  onEdit,
  onDelete,
  onInvoices,
  totalCount,
  currentPage,
  setCurrentPage,
  limit,
  rentalStatuses,
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
              <TableCell align='center'>Rental ID</TableCell>
              <TableCell align='center'>User Email</TableCell>
              <TableCell align='center'>Username</TableCell>
              <TableCell align='center'>Apartment</TableCell>
              <TableCell align='center'>Room Type</TableCell>
              <TableCell align='center'>Price</TableCell>
              <TableCell align='center'>Deposit</TableCell>
              <TableCell align='center'>Status</TableCell>
              <TableCell align='center'>Actions</TableCell>
              <TableCell align='center'>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rentals.map(rental => (
              <TableRow key={rental.rental_id} hover>
                <TableCell align='center'>{rental.rental_id}</TableCell>
                <TableCell align='center'>{rental.user.user_email}</TableCell>
                <TableCell align='center'>{rental.user.user_name}</TableCell>
                <TableCell align='center'>
                  {rental.room.available_room_type.apartment_name}
                </TableCell>
                <TableCell align='center'>
                  {rental.room.available_room_type.room_type.room_type_name}
                </TableCell>
                <TableCell align='center'>
                  {rental.room.available_room_type.available_room_type_price}
                </TableCell>
                <TableCell align='center'>
                  {
                    rental.room.available_room_type
                      .available_room_type_deposit_amount
                  }
                </TableCell>
                <TableCell align='center'>
                  <Select
                    className='w-32'
                    value={rental.rental_status.rental_status_id}
                    onChange={e => onEdit(rental, e.target.value)}
                    disabled={statusesLoading}
                  >
                    {rentalStatuses.map(status => (
                      <MenuItem
                        key={status.rental_status_id}
                        value={status.rental_status_id}
                      >
                        {status.rental_status_name}
                      </MenuItem>
                    ))}
                  </Select>
                </TableCell>
                <TableCell align='center'>
                  <Button
                    variant='outlined'
                    color='error'
                    onClick={() => onDelete(rental.rental_id)}
                  >
                    Delete
                  </Button>
                </TableCell>
                <TableCell align='center'>
                  <Button
                    variant='contained'
                    color='primary'
                    onClick={() => onInvoices(rental.rental_id)}
                  >
                    Invoices
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
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

export default RentalTable
