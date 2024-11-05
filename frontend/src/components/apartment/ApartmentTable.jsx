import React from 'react'
import {
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Button,
  Pagination,
  Paper,
} from '@mui/material'

function ApartmentTable({
  apartments,
  onEdit,
  onDelete,
  onView,
  totalCount,
  currentPage,
  setCurrentPage,
  limit,
}) {
  const totalPages = Math.ceil(totalCount / limit)

  const handlePageChange = (event, newPage) => {
    setCurrentPage(newPage)
  }

  return (
    <Paper elevation={3} className='p-4 w-full'>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell align='center'>Name</TableCell>
            <TableCell align='center'>Address</TableCell>
            <TableCell align='center'>Date Built</TableCell>
            <TableCell align='center'>Postal Code</TableCell>
            <TableCell align='center'>Capacity</TableCell>
            <TableCell align='center'>Image</TableCell>
            <TableCell align='center'>View</TableCell>
            <TableCell align='center'>Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {apartments.map(apartment => (
            <TableRow key={apartment.apartment_id} hover>
              <TableCell align='center'>{apartment.apartment_name}</TableCell>
              <TableCell align='center'>
                {apartment.apartment_address}
              </TableCell>
              <TableCell align='center'>
                {apartment.apartment_date_built}
              </TableCell>
              <TableCell align='center'>
                {apartment.apartment_postal_code}
              </TableCell>
              <TableCell align='center'>
                {apartment.apartment_capacity}
              </TableCell>
              <TableCell align='center'>
                <img
                  src={`${import.meta.env.VITE_BASE_URL}/${apartment.apartment_image}`}
                  alt='Apartment'
                  style={{
                    width: 64,
                    height: 64,
                    objectFit: 'cover',
                    borderRadius: 4,
                  }}
                />
              </TableCell>
              <TableCell align='center'>
                <Button
                  variant='contained'
                  color='primary'
                  onClick={() => onView(apartment.apartment_id)}
                >
                  View
                </Button>
              </TableCell>
              <TableCell align='center'>
                <Button
                  variant='outlined'
                  color='primary'
                  onClick={() => onEdit(apartment)}
                  style={{ marginRight: 8 }}
                >
                  Edit
                </Button>
                <Button
                  variant='outlined'
                  color='error'
                  onClick={() => onDelete(apartment.apartment_id)}
                >
                  Delete
                </Button>
              </TableCell>
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
  )
}

export default ApartmentTable
