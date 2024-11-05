import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/rentals`

const fetchAll = async (rentalId, limit = 10, offset = 0) => {
  try {
    const response = await axios.get(`${BASE_URL}/${rentalId}/invoices`, {
      params: { limit, offset },
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching invoices:', error)
    throw error
  }
}

const fetchById = async (rentalId, invoiceId) => {
  try {
    const response = await axios.get(
      `${BASE_URL}/${rentalId}/invoices/${invoiceId}`,
      {
        headers: {
          Authorization: `Bearer ${getItem('adminToken')}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error fetching invoice:', error)
    throw error
  }
}

const create = async (rentalId, invoiceData) => {
  try {
    const response = await axios.post(
      `${BASE_URL}/${rentalId}/invoices`,
      invoiceData,
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${getItem('adminToken')}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error creating invoice:', error)
    throw error
  }
}

const update = async (rentalId, invoiceId, invoiceData) => {
  try {
    const response = await axios.put(
      `${BASE_URL}/${rentalId}/invoices/${invoiceId}`,
      invoiceData,
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${getItem('adminToken')}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error updating invoice:', error)
    throw error
  }
}

const del = async (rentalId, invoiceId) => {
  try {
    await axios.delete(`${BASE_URL}/${rentalId}/invoices/${invoiceId}`, {
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
  } catch (error) {
    console.error('Error deleting invoice:', error)
    throw error
  }
}

export { fetchAll, fetchById, create, update, del }
