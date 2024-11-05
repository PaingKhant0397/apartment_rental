/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from 'react'
import {
  fetchAll,
  fetchById,
  insert,
  update,
  del,
} from '../services/rentalServices'
import useNotification from './useNotificaiton'

const useRentals = () => {
  const [rentals, setRentals] = useState([])
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
      setRentals(data.data)
      setPagination(prev => ({ ...prev, total: data.total_count }))
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load rentals')
    } finally {
      setLoading(false)
    }
  }

  const getById = async id => {
    setLoading(true)
    try {
      const Rental = await fetchById(id)
      return Rental
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load Rental details')
    } finally {
      setLoading(false)
    }
  }

  const create = async data => {
    setLoading(true)
    try {
      const newRental = await insert(data)
      setRentals(prev => [...prev, newRental])
      notify('success', 'Rental added successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to add Rental')
    } finally {
      setLoading(false)
    }
  }

  const edit = async data => {
    setLoading(true)
    try {
      const updatedRental = await update(data.rental_id, data)
      console.log(updatedRental)
      getAll()
      notify('success', 'Rental updated successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to update Rental')
    } finally {
      setLoading(false)
    }
  }

  const remove = async id => {
    setLoading(true)
    try {
      await del(id)
      setRentals(prevrentals =>
        prevrentals.filter(Rental => Rental.rental_id !== id),
      )
      notify('success', 'Rental deleted successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to delete Rental')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    getAll()
  }, [pagination.limit, pagination.offset])

  return {
    rentals,
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

export default useRentals
