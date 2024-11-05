import { useEffect, useState } from 'react'
import {
  fetchApartments,
  fetchApartmentById,
  createApartment,
  updateApartment,
  deleteApartment,
} from '../services/apartmentServices'
import useNotification from './useNotificaiton'

const useApartments = () => {
  const [apartments, setApartments] = useState([])
  const [totalCount, setTotalCount] = useState(0)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [limit, setLimit] = useState(5)
  const [currentPage, setCurrentPage] = useState(1)
  const notify = useNotification()

  const getAllApartments = async (page = 1) => {
    setLoading(true)
    try {
      const offset = (page - 1) * limit
      const data = await fetchApartments(limit, offset)
      setApartments(data.data)
      setTotalCount(data.total_count)
      setCurrentPage(page)
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load apartments')
    } finally {
      setLoading(false)
    }
  }

  const createFormData = apartment => {
    const formData = new FormData()
    Object.keys(apartment).forEach(key => {
      formData.append(key, apartment[key])
    })
    return formData
  }

  const addApartment = async apartment => {
    try {
      const formData = createFormData(apartment) // Create FormData
      const newApartment = await createApartment(formData) // Send as form-data
      setApartments(prev => [...prev, newApartment])
      notify('success', 'Apartment Registered successfully')
    } catch (err) {
      setError(err)
      console.error(err)
      notify('error', 'Failed to add apartment')
    }
  }

  const editApartment = async (id, updatedApartment) => {
    try {
      const formData = createFormData(updatedApartment) // Create FormData for update
      const newApartment = await updateApartment(id, formData)
      // console.log('new updated', newApartment)
      setApartments(prev =>
        prev.map(apt => (apt.apartment_id === id ? newApartment : apt)),
      )
      notify('success', 'Apartment updated successfully')
    } catch (err) {
      setError(err)
      console.error(err)
      notify('error', 'Failed to update apartment')
    }
  }

  const removeApartment = async id => {
    try {
      await deleteApartment(id)
      setApartments(prev => prev.filter(apt => apt.apartment_id !== id))
      notify('success', 'Apartment deleted successfully')
    } catch (err) {
      setError(err)
      console.error(err)
      notify('error', 'Failed to delete apartment')
    }
  }

  const getApartment = async id => {
    try {
      const fetchedApartment = await fetchApartmentById(id)
      return fetchedApartment
    } catch (err) {
      setError(err)
      console.error(err)
      notify('error', 'Failed to load apartment details')
    }
  }

  return {
    apartments,
    totalCount,
    loading,
    error,
    limit,
    currentPage,
    getAllApartments,
    setCurrentPage,
    addApartment,
    editApartment,
    removeApartment,
    getApartment,
  }
}

export default useApartments
