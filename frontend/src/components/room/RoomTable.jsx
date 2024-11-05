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

function RoomTable({
  rooms,
  onEdit,
  onDelete,
  onRegister,
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
    <div className='p-4 w-full'>
      <div className='mb-6'>
        <Button color='secondary' onClick={() => onRegister()}>
          Add Room
        </Button>
      </div>

      <Paper elevation={3} className='p-4 w-full'>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell align='center'>Room No</TableCell>
              <TableCell align='center'>Room Size</TableCell>
              <TableCell align='center'>Floor No</TableCell>
              <TableCell align='center'>Status</TableCell>
              <TableCell align='center'>Room Type</TableCell>
              <TableCell align='center'>Price</TableCell>
              <TableCell align='center'>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rooms.map(room => (
              <TableRow key={room.room_id} hover>
                <TableCell align='center'>{room.room_no}</TableCell>
                <TableCell align='center'>{room.room_size}</TableCell>
                <TableCell align='center'>{room.room_floor_no}</TableCell>
                <TableCell align='center'>
                  {room.status.room_status_name}
                </TableCell>
                <TableCell align='center'>
                  {room.available_room_type.room_type.room_type_name}
                </TableCell>
                <TableCell align='center'>
                  {room.available_room_type.available_room_type_price}
                </TableCell>
                <TableCell align='center'>
                  <Button
                    variant='outlined'
                    color='primary'
                    onClick={() => onEdit(room)}
                    style={{ marginRight: 8 }}
                  >
                    Edit
                  </Button>
                  <Button
                    variant='outlined'
                    color='error'
                    onClick={() => onDelete(room.room_id)}
                  >
                    Delete
                  </Button>
                  {/* <Button
                  variant='contained'
                  color='primary'
                  onClick={() => onView(room.room_id)}
                >
                  View
                </Button> */}
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
    </div>
  )
}

export default RoomTable
