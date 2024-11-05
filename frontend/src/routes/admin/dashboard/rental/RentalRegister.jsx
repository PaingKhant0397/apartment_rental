import { useEffect, useState } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import useBookings from '../../../../hooks/useBooking'
import useRooms from '../../../../hooks/useRooms'
import useRentals from '../../../../hooks/useRentals'
import RentalForm from '../../../../components/rental/RentalForm'

function RentalRegister() {
  const location = useLocation() // Use location to get the state
  const { bookingId } = location.state || {} // Access bookingId from state
  const [bookingData, setBookingData] = useState(null)
  const [rooms, setRooms] = useState([])
  const [totalCount, setTotalCount] = useState(0)
  const [loading, setLoading] = useState(true)
  const [selectedRoom, setSelectedRoom] = useState()
  const navigate = useNavigate()
  const { getById } = useBookings()
  const { getAvailableRooms } = useRooms() // Your method to get available rooms
  const { create } = useRentals() // Method to create a rental

  useEffect(() => {
    if (!bookingId) {
      console.error('Booking ID is undefined')
      return // Exit if bookingId is not available
    }

    const fetchBookingData = async () => {
      try {
        const data = await getById(bookingId)
        setBookingData(data)

        if (data) {
          const availableRoomTypeId = data.room_type.available_room_type_id
          const apartmentID = data.room_type.apartment_id
          const result = await getAvailableRooms(
            apartmentID,
            availableRoomTypeId,
          )
          setRooms(result.data)
          setTotalCount(result.total_count)
        }
      } catch (error) {
        console.error('Error fetching booking data:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchBookingData()
  }, [bookingId])

  const handleBack = () => {
    navigate('/admin/dashboard/bookings') // Adjust the path as needed
  }

  const handleRoomChange = e => {
    setSelectedRoom(e.target.value) // Update selected room from the dropdown
  }

  const handleSubmit = async e => {
    e.preventDefault()

    if (selectedRoom) {
      const rentalData = {
        room: selectedRoom,
        rental_status: {
          rental_status_id: 1,
          rental_status_name: 'Active',
        },
        user: bookingData.user,
        rental_start_date: new Date().toISOString().split('T')[0], // Set rental start date
        rental_end_date: new Date(
          new Date().setFullYear(new Date().getFullYear() + 1),
        )
          .toISOString()
          .split('T')[0], // Set rental end date
      }

      try {
        // console.log(rentalData)
        await create(rentalData) // Call the method to create rental
        // navigate('/rentals') // Navigate to rentals page after successful registration
      } catch (error) {
        console.error('Error registering rental:', error)
      }
    }
  }

  if (loading) return <div>Loading...</div>

  return (
    <RentalForm
      bookingData={bookingData}
      rooms={rooms}
      onBack={handleBack}
      onSubmit={handleSubmit} // Pass the submit handler to the form
      selectedRoom={selectedRoom}
      handleRoomChange={handleRoomChange} // Pass room change handler to the form
    />
  )
}

export default RentalRegister
