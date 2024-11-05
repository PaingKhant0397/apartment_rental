import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button } from '@mui/material'
import useRentals from '../../../../hooks/useRentals' // Assuming this hook is for rental data
import RentalTable from '../../../../components/rental/RentalTable' // Assuming you will create this component
import Loading from '../../../../components/Loading'
import useRentalStatuses from '../../../../hooks/useRentalStatuses'

function RentalList() {
  const { rentals, loading, edit, remove, pagination, setPagination } =
    useRentals()
  const navigate = useNavigate()
  const { rentalStatuses, loading: statusesLoading } = useRentalStatuses()

  const onDelete = id => {
    remove(id)
  }

  const onEdit = (rental, status_id) => {
    try {
      const newRental = { ...rental }
      newRental.rental_status.rental_status_id = status_id
      edit(newRental)
    } catch (err) {
      console.error(err)
    }
  }

  const onInvoices = rentalId => {
    navigate(`/admin/dashboard/rentals/${rentalId}/invoices`) // Navigate to rental details page
  }

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <RentalTable
        rentals={rentals}
        rentalStatuses={rentalStatuses}
        statusesLoading={statusesLoading}
        onDelete={onDelete}
        onEdit={onEdit}
        onInvoices={onInvoices}
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

export default RentalList
