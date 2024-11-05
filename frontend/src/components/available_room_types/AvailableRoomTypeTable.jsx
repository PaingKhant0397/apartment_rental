import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Button,
  Box,
} from '@mui/material'

function AvailableRoomTypeTable({ data, onEdit, onDelete, onAdd }) {
  return (
    <Box width='100%' minHeight='100vh'>
      <Box display='flex' justifyContent='flex-start' mb={3}>
        <Button variant='contained' color='primary' onClick={onAdd}>
          Add Available Room Type
        </Button>
      </Box>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Room Type</TableCell>
              <TableCell>Price</TableCell>
              <TableCell>Deposit</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {data?.map(availableRoomType => (
              <TableRow key={availableRoomType.available_room_type_id}>
                <TableCell>
                  {availableRoomType.room_type.room_type_name}
                </TableCell>
                <TableCell>
                  {availableRoomType.available_room_type_price}
                </TableCell>
                <TableCell>
                  {availableRoomType.available_room_type_deposit_amount}
                </TableCell>
                <TableCell>
                  <Button
                    variant='outlined'
                    color='primary'
                    onClick={() => onEdit(availableRoomType)}
                    sx={{ mr: 1 }}
                  >
                    Edit
                  </Button>
                  <Button
                    variant='outlined'
                    color='error'
                    onClick={() =>
                      onDelete(
                        availableRoomType.apartment_id,
                        availableRoomType.available_room_type_id,
                      )
                    }
                  >
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  )
}

export default AvailableRoomTypeTable
