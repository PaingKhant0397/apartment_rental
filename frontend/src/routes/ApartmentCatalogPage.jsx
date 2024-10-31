import { Container } from '@mui/material'
import ApartmentCatalog from '../components/apartment/ApartmentCatalog'

function ApartmentCatalogPage() {
  return (
    <Container maxWidth='lg' sx={{ padding: '2rem 0' }}>
      <ApartmentCatalog />
    </Container>
  )
}

export default ApartmentCatalogPage
