import { useEffect, useState } from 'react'
import {
  fetchAll,
  fetchById,
  insert,
  update,
  del,
} from '../services/bookingServices'
import useNotification from './useNotificaiton'

const useBookings = apartmentId => {
  const [bookings, setBookings] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [pagination, setPagination] = useState({
    limit: 10,
    offset: 0,
    total: 0,
  })

  const notify = useNotification()

  const getAll = async () => {
    setLoading(true)
    try {
      const data = await fetchAll(pagination.limit, pagination.offset)
      setBookings(data.data)
      setPagination(prev => ({ ...prev, total: data.total_count }))
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load Bookings')
    } finally {
      setLoading(false)
    }
  }

  const getById = async BookingId => {
    setLoading(true)
    try {
      const Booking = await fetchById(BookingId)
      return Booking
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load Booking details')
    } finally {
      setLoading(false)
    }
  }

  const create = async BookingData => {
    setLoading(true)
    try {
      const newBooking = await insert(BookingData)
      setBookings(prev => [...prev, newBooking])
      notify('success', 'Booking added successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to add Booking')
    } finally {
      setLoading(false)
    }
  }

  const edit = async BookingData => {
    setLoading(true)
    try {
      const updatedBooking = await update(BookingData.booking_id, BookingData)
      console.log(updatedBooking)
      getAll()
      // setBookings(prevBookings =>
      //   prevBookings.map(Booking =>
      //     Booking.booking_id === BookingData.booking_id
      //       ? updatedBooking
      //       : Booking,
      //   ),
      // )
      notify('success', 'Booking updated successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to update Booking')
    } finally {
      setLoading(false)
    }
  }

  const remove = async BookingId => {
    setLoading(true)
    try {
      await del(BookingId)
      setBookings(prevBookings =>
        prevBookings.filter(Booking => Booking.booking_id !== BookingId),
      )
      notify('success', 'Booking deleted successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to delete Booking')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    getAll()
  }, [pagination.limit, pagination.offset])

  return {
    bookings,
    loading,
    error,
    pagination,
    getById,
    create,
    edit,
    remove,
    setPagination,
  }
}

export default useBookings
