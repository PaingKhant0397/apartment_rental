import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button } from '@mui/material'
import useBookings from '../../../../hooks/useBooking'
import BookingTable from '../../../../components/booking/BookingTable'
import Loading from '../../../../components/Loading'
import useBookingStatuses from '../../../../hooks/useBookingStatuses'

function BookingList() {
  const { bookings, loading, edit, remove, pagination, setPagination } =
    useBookings()
  const navigate = useNavigate()
  const { bookingStatuses, loading: statusesLoading } = useBookingStatuses()

  const onDelete = id => {
    remove(id)
  }

  const onEdit = (booking, status_id) => {
    try {
      const newBooking = { ...booking }
      newBooking.status.booking_status_id = status_id
      edit(newBooking)
    } catch (err) {
      console.error(err)
    }
  }

  // New onRental function
  const onRental = bookingId => {
    // console.log(bookingId)
    navigate('/admin/dashboard/rentals/register', { state: { bookingId } }) // Navigate with booking data
  }

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <BookingTable
        bookings={bookings}
        bookingStatuses={bookingStatuses}
        statusesLoading={statusesLoading}
        onDelete={onDelete}
        onEdit={onEdit}
        onRental={onRental} // Pass onRental to BookingTable
        totalCount={pagination.total}
        currentPage={pagination.offset / pagination.limit + 1}
        setCurrentPage={page =>
          setPagination(prev => ({
            ...prev,
            offset: (page - 1) * pagination.limit,
          }))
        }
        limit={pagination.limit}
      />
    </div>
  )
}

export default BookingList
