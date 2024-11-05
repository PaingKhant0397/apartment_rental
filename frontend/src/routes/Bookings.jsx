/* eslint-disable camelcase */
import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { Button } from '@mui/material'
import useBookings from '../hooks/useBooking'

import Loading from '../components/Loading'
import useBookingStatuses from '../hooks/useBookingStatuses'
import BookingTableClient from '../components/booking/BookingTableClient'

function Bookings() {
  const { bookings, loading, edit, remove, pagination, setPagination } =
    useBookings()
  // console.log('bookings', bookings)
  const navigate = useNavigate()
  const { bookingStatuses, loading: statusesLoading } = useBookingStatuses()
  // useEffect(() => {
  //   getAllbookings()
  // }, [pagination.limit, pagination.offset]) // Fetch bookings when pagination changes

  const onDelete = id => {
    remove(id)
  }

  const onEdit = (booking, status_id) => {
    try {
      const newBooking = { ...booking }
      newBooking.status.booking_status_id = status_id
      edit(newBooking)
      console.log('booking', newBooking)
      console.log('status', status_id)
    } catch (err) {
      console.error(err)
    }
  }

  const onRegister = () => {
    navigate(`/admin/dashboard/bookings/register`)
  }

  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <BookingTableClient
        bookings={bookings}
        bookingStatuses={bookingStatuses}
        statusesLoading={statusesLoading}
        onDelete={onDelete}
        onEdit={onEdit}
        onRegister={onRegister}
        totalCount={pagination.total}
        currentPage={pagination.offset / pagination.limit + 1} // Calculate current page
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

export default Bookings
