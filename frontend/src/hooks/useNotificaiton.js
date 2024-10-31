import { toast } from 'react-toastify'

const useNotification = () => {
  const notify = (type, message) => {
    if (type === 'success') {
      toast.success(message)
    } else if (type === 'error') {
      toast.error(message)
    } else {
      toast(message)
    }
  }

  return notify
}

export default useNotification
