import Button from '../Button'

function ApartmentTable({ apartments, onEdit, onDelete, onView }) {
  // console.log(apartments)
  if (apartments.length === 0) {
    return <p>No apartments available.</p>
  }

  return (
    <table className='bg-white p-8 rounded-lg shadow-md w-full h-fit overflow-hidden'>
      <thead>
        <tr className='bg-gray-300'>
          <th className='py-2 px-4 border-b'>Name</th>
          <th className='py-2 px-4 border-b'>Address</th>
          <th className='py-2 px-4 border-b'>Date Built</th>
          <th className='py-2 px-4 border-b'>Postal Code</th>
          <th className='py-2 px-4 border-b'>Capacity</th>
          <th className='py-2 px-4 border-b'>Image</th>
          <th className='py-2 px-4 border-b'>View</th>
          <th className='py-2 px-4 border-b'>Actions</th>
        </tr>
      </thead>
      <tbody>
        {apartments.map(apartment => (
          <tr key={apartment.apartment_id} className='text-center'>
            <td className='py-2 px-4 border-b'>{apartment.apartment_name}</td>
            <td className='py-2 px-4 border-b'>
              {apartment.apartment_address}
            </td>
            <td className='py-2 px-4 border-b'>
              {apartment.apartment_date_built}
            </td>
            <td className='py-2 px-4 border-b'>
              {apartment.apartment_postal_code}
            </td>
            <td className='py-2 px-4 border-b'>
              {apartment.apartment_capacity}
            </td>
            <td className='py-2 px-4 border-b'>
              <img
                src={`${import.meta.env.VITE_BASE_URL}/${apartment.apartment_image}`}
                alt='an apartment'
                className='w-16 h-16 object-cover'
              />
            </td>
            <td className='py-2 px-4 border-b'>
              <Button
                variant='primary'
                onClick={() => onView(apartment.apartment_id)}
              >
                View
              </Button>
            </td>

            <td className='py-2 px-4 border-b space-x-2'>
              <Button variant='secondary' onClick={() => onEdit(apartment)}>
                Edit
              </Button>
              <Button
                variant='danger'
                onClick={() => onDelete(apartment.apartment_id)}
              >
                Delete
              </Button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

export default ApartmentTable
