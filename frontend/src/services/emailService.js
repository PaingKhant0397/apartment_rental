import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/send-email`

const EmailService = {
  sendEmail: async emailData => {
    try {
      const response = await axios.post(BASE_URL, emailData, {
        headers: {
          'Content-Type': 'application/json',
          // Include any other necessary headers, like authorization if needed
        },
      })
      return response.data // Return the response data
    } catch (error) {
      throw error.response?.data || error.message // Throw error for handling in the hook
    }
  },
}

export default EmailService
