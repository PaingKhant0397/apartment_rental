/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from 'react'

import { useParams } from 'react-router-dom'
import ApartmentForm from '../../../../components/apartment/ApartmentForm'
import useApartments from '../../../../hooks/useApartments'
import Loading from '../../../../components/Loading'

function ApartmentUpdate() {
  const initialData = {
    apartment_id: '',
    apartment_name: '',
    apartent_address: '',
    apartment_desc: '',
    apartment_date_built: '',
    apartment_postal_code: '',
    apartment_capacity: '',
    apartment_image: null,
  }

  const [apartment, setApartment] = useState(initialData)
  const { id } = useParams()
  const { loading, getApartment, editApartment } = useApartments()

  useEffect(() => {
    const getApt = async () => {
      const apt = await getApartment(id)
      setApartment(apt)
    }
    getApt()
  }, [id])

  const handleOnSubmit = updatedApartment => {
    editApartment(updatedApartment.apartment_id, updatedApartment)
  }

  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <ApartmentForm
        onSubmit={handleOnSubmit}
        initialData={apartment}
        reset={false}
      />
    </div>
  )
}

export default ApartmentUpdate
