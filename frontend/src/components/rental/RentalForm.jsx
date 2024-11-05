import React from 'react'
import {
  Button,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Typography,
  Card,
  CardContent,
  CardActions,
  CircularProgress,
} from '@mui/material'

function RentalForm({
  bookingData,
  rooms,
  onBack,
  onSubmit,
  selectedRoom,
  handleRoomChange,
  loading, // added loading state prop for progress indication
}) {
  return (
    <Card variant='outlined' sx={{ width: 'full', margin: 'auto', mt: 4 }}>
      <CardContent>
        {loading ? ( // Show loading spinner while data is loading
          <CircularProgress />
        ) : (
          <>
            {bookingData && (
              <Typography variant='h6' gutterBottom>
                Registering rental for user {bookingData.user.user_email}
              </Typography>
            )}
            {rooms.length === 0 ? (
              <Typography variant='body1'>
                No room of type {bookingData.room_type.room_type_name} is
                currently available.
              </Typography>
            ) : (
              <form onSubmit={onSubmit}>
                <FormControl fullWidth variant='outlined' margin='normal'>
                  <InputLabel>Select a room</InputLabel>
                  <Select
                    value={selectedRoom || ''}
                    onChange={handleRoomChange}
                    label='Select a room'
                  >
                    {rooms.map(room => (
                      <MenuItem key={room.room_id} value={room}>
                        Room {room.room_no} - Type{' '}
                        {room.available_room_type.room_type.room_type_name} -
                        Price $
                        {room.available_room_type.available_room_type_price}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
                <CardActions>
                  <Button
                    type='submit'
                    variant='contained'
                    color='primary'
                    disabled={!selectedRoom}
                  >
                    Register Rental
                  </Button>
                  <Button
                    type='button'
                    variant='outlined'
                    color='secondary'
                    onClick={onBack}
                  >
                    Go Back
                  </Button>
                </CardActions>
              </form>
            )}
          </>
        )}
      </CardContent>
    </Card>
  )
}

export default RentalForm
