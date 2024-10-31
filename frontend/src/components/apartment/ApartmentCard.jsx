/* eslint-disable camelcase */
// src/components/ApartmentCard.js
import React from 'react'
import {
  Card,
  CardMedia,
  CardContent,
  Typography,
  List,
  ListItem,
  ListItemText,
  Button,
  Box,
  Divider,
} from '@mui/material'
import { useNavigate } from 'react-router-dom'

function ApartmentCard({ apartment }) {
  const {
    apartment_id,
    apartment_name,
    apartment_image,
    apartment_address,
    available_room_types,
  } = apartment

  const navigate = useNavigate()

  const handleViewDetails = () => {
    navigate(`/apartments/${apartment_id}`)
  }

  if (available_room_types.length === 0) {
    return null
  }

  return (
    <Card
      sx={{
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: 3,
        transition: 'transform 0.2s ease-in-out',
        '&:hover': {
          transform: 'scale(1.02)',
        },
      }}
    >
      <CardMedia
        component='img'
        height='200'
        image={
          apartment_image
            ? `${import.meta.env.VITE_BASE_URL}/${apartment_image}`
            : 'https://via.placeholder.com/400'
        }
        alt={apartment_name}
      />
      <CardContent
        sx={{ flexGrow: 1, p: 2, display: 'flex', flexDirection: 'column' }}
      >
        <Typography
          variant='h6'
          color='primary'
          sx={{ mb: 1, fontWeight: 'bold' }}
        >
          {apartment_name}
        </Typography>
        <Typography variant='body2' color='textSecondary' sx={{ mb: 2 }}>
          Location: {apartment_address}
        </Typography>

        <Divider sx={{ mb: 2 }} />

        {/* Available Room Types */}
        <Typography
          variant='subtitle1'
          gutterBottom
          color='primary'
          sx={{ fontWeight: 'medium' }}
        >
          Available Room Types
        </Typography>
        {available_room_types.length > 0 ? (
          <List dense sx={{ py: 0, mb: 2 }}>
            {available_room_types.map(room => (
              <ListItem key={room.available_room_type_id} disableGutters>
                <ListItemText
                  primary={`${room.room_type.room_type_name} - $${room.available_room_type_price.toLocaleString()}`}
                  primaryTypographyProps={{ fontSize: '0.875rem' }}
                />
              </ListItem>
            ))}
          </List>
        ) : (
          <Typography variant='body2' color='textSecondary'>
            No available room types
          </Typography>
        )}

        {/* Action Button */}
        <Box sx={{ mt: 'auto', textAlign: 'center' }}>
          <Button
            variant='contained'
            color='primary'
            fullWidth
            onClick={handleViewDetails}
            sx={{
              fontWeight: 'bold',
              '&:hover': {
                color: 'white',
              },
            }}
          >
            View Details
          </Button>
        </Box>
      </CardContent>
    </Card>
  )
}

export default ApartmentCard
