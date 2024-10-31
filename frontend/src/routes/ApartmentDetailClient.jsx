/* eslint-disable react-hooks/exhaustive-deps */
// src/components/ApartmentDetailClient.js
import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Container,
  Typography,
  Card,
  CardContent,
  CardMedia,
  Button,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  List,
  ListItem,
  ListItemText,
  CircularProgress,
  Box,
  Divider,
} from '@mui/material'
import useApartments from '../hooks/useApartments'

function ApartmentDetailClient() {
  const { id } = useParams()
  const [apartment, setApartment] = useState(null)
  const [selectedRoomType, setSelectedRoomType] = useState('')
  const navigate = useNavigate()
  const { getApartment } = useApartments()

  useEffect(() => {
    const fetchApartment = async () => {
      const apt = await getApartment(id)
      setApartment(apt)
    }
    fetchApartment()
  }, [id])

  const handleRoomTypeChange = event => {
    setSelectedRoomType(event.target.value)
  }

  const handleBookApartment = () => {
    if (selectedRoomType) {
      navigate(`/booking/${id}?roomType=${selectedRoomType}`)
    }
  }

  if (!apartment) {
    return (
      <Box
        display='flex'
        justifyContent='center'
        alignItems='center'
        height='100vh'
      >
        <CircularProgress />
      </Box>
    )
  }

  return (
    <Container maxWidth='md' sx={{ py: 4 }}>
      <Card sx={{ boxShadow: 3 }}>
        <CardMedia
          component='img'
          height='300'
          image={
            apartment.apartment_image
              ? `${import.meta.env.VITE_BASE_URL}/${apartment.apartment_image}`
              : 'https://via.placeholder.com/400'
          }
          alt={apartment.apartment_name}
          sx={{ objectFit: 'cover' }}
        />
        <CardContent>
          <Typography
            variant='h4'
            gutterBottom
            color='primary'
            fontWeight='bold'
          >
            {apartment.apartment_name}
          </Typography>
          <Typography variant='body1' paragraph>
            {apartment.apartment_desc}
          </Typography>
          <Typography variant='subtitle1' color='textSecondary'>
            Location: {apartment.apartment_address}
          </Typography>
          <Typography variant='subtitle1' color='textSecondary'>
            Built Date: {apartment.apartment_date_built}
          </Typography>
          <Typography variant='subtitle1' color='textSecondary' gutterBottom>
            Capacity: {apartment.apartment_capacity}
          </Typography>

          <Divider sx={{ my: 2 }} />

          <Typography variant='h6' color='primary' gutterBottom>
            Available Room Types
          </Typography>
          {apartment.available_room_types.length > 0 ? (
            <List dense sx={{ mb: 2 }}>
              {apartment.available_room_types.map(room => (
                <ListItem key={room.available_room_type_id} disableGutters>
                  <ListItemText
                    primary={`${room.room_type.room_type_name} - $${room.available_room_type_price.toLocaleString()}`}
                  />
                </ListItem>
              ))}
            </List>
          ) : (
            <Typography variant='body2' color='textSecondary'>
              No available room types
            </Typography>
          )}

          <FormControl fullWidth sx={{ mt: 2 }}>
            <InputLabel id='room-type-select-label'>
              Select Room Type To Book
            </InputLabel>
            <Select
              labelId='room-type-select-label'
              value={selectedRoomType}
              onChange={handleRoomTypeChange}
              label='Select Room Type To Book'
            >
              {apartment.available_room_types.map(room => (
                <MenuItem
                  key={room.available_room_type_id}
                  value={room.available_room_type_id}
                >
                  {room.room_type.room_type_name} - $
                  {room.available_room_type_price.toLocaleString()}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <Button
            variant='contained'
            color='primary'
            fullWidth
            sx={{ mt: 3, fontWeight: 'bold' }}
            onClick={handleBookApartment}
            disabled={!selectedRoomType}
          >
            Book Apartment
          </Button>
        </CardContent>
      </Card>
    </Container>
  )
}

export default ApartmentDetailClient
