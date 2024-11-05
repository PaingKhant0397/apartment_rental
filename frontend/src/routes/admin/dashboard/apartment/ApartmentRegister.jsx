import { useState } from 'react'
import { toast } from 'react-toastify'

import ApartmentForm from '../../../../components/apartment/ApartmentForm'
import useApartments from '../../../../hooks/useApartments'
import Loading from '../../../../components/Loading'

function ApartmentRegister() {
  const initialData = {
    apartment_name: '',
    apartment_address: '',
    apartment_desc: '',
    apartment_date_built: '',
    apartment_postal_code: '',
    apartment_capacity: '',
    apartment_image: null,
  }
  const { loading, error, addApartment } = useApartments()

  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <ApartmentForm onSubmit={addApartment} initialData={initialData} reset />
    </div>
  )
}

export default ApartmentRegister
