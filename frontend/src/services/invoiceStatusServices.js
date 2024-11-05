import axios from 'axios'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/invoice_statuses`

export const fetchAllInvoiceStatuses = async () => {
  const response = await axios.get(BASE_URL)
  return response.data
}

export const fetchInvoiceStatusById = async id => {
  const response = await axios.get(`${BASE_URL}/${id}`)
  return response.data
}
