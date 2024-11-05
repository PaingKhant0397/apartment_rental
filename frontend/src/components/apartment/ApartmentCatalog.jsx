// src/components/ApartmentCatalog.js
import { useEffect } from 'react'
import {
  Container,
  Typography,
  Box,
  Button,
  Grid,
  Card,
  CardContent,
} from '@mui/material'
import ApartmentCard from './ApartmentCard'
import useApartments from '../../hooks/useApartments'

function ApartmentCatalog() {
  // Sample Data (replace this with your data fetching method)
  const { apartments, loading, error, getAllApartments } = useApartments()

  useEffect(() => {
    getAllApartments()
    // console.log(apartments)
  }, [])

  return (
    <Box id='catalog' sx={{ pt: 6 }}>
      <Typography variant='h4' align='center' gutterBottom>
        Available Apartments
      </Typography>
      <Typography
        variant='body1'
        align='center'
        color='textSecondary'
        paragraph
      >
        Explore our range of available apartments and find the perfect space to
        call home.
      </Typography>
      <Grid container spacing={4} sx={{ marginTop: '2rem' }}>
        {apartments.map(apartment => {
          if (
            apartment.available_room_types &&
            apartment.available_room_types.length !== 0
          ) {
            return (
              <Grid item xs={12} sm={6} md={4} key={apartment.apartment_id}>
                <ApartmentCard apartment={apartment} />
              </Grid>
            )
          }
        })}
      </Grid>
    </Box>
  )
}

export default ApartmentCatalog
