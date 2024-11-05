// hooks/useEmail.js
import { useState } from 'react'
import EmailService from '../services/emailService'
import useNotification from './useNotificaiton'

const useEmail = () => {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const notify = useNotification()
  const sendEmail = async emailData => {
    setLoading(true)
    setError(null) // Reset error state

    try {
      const result = await EmailService.sendEmail(emailData)
      // return result // Return result on success
      notify('success', 'Mail sent successfully')
    } catch (err) {
      setError(err) // Set error on failure
    } finally {
      setLoading(false) // Reset loading state
    }
  }

  return { sendEmail, loading, error }
}

export default useEmail
