/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import useApartments from '../../../../hooks/useApartments'
import ApartmentTable from '../../../../components/apartment/ApartmentTable'
import Loading from '../../../../components/Loading'

function ApartmentList() {
  const {
    apartments,
    loading,
    removeApartment,
    getAllApartments,
    totalCount,
    currentPage,
    setCurrentPage,
    limit,
  } = useApartments()
  const navigate = useNavigate()

  useEffect(() => {
    getAllApartments(currentPage)
  }, [currentPage])

  const onDelete = id => {
    removeApartment(id)
  }

  const onEdit = apartment => {
    navigate(`/admin/dashboard/apartments/${apartment.apartment_id}/update`)
  }

  const onView = id => {
    navigate(`/admin/dashboard/apartments/${id}`)
  }

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      {/* {loading && <Loading />} */}
      <ApartmentTable
        apartments={apartments}
        onDelete={onDelete}
        onEdit={onEdit}
        onView={onView}
        totalCount={totalCount}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        limit={limit}
      />
    </div>
  )
}

export default ApartmentList
