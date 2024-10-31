import Button from '../Button'

function AvailableRoomTypeTable({ data, onEdit, onDelete, onAdd }) {
  if (data?.length === 0) {
    return <p>No Room Types available.</p>
  }

  return (
    <div className='w-full min-h-screen'>
      <div className='flex justify-start mb-6'>
        <Button variant='primary' onClick={() => onAdd()}>
          Add Available Room Type
        </Button>
      </div>
      <table className='bg-white p-8 rounded-lg shadow-md w-full h-fit overflow-hidden'>
        <thead>
          <tr className='bg-gray-300'>
            <th className='py-2 px-4 border-b'>Room Type</th>
            <th className='py-2 px-4 border-b'>Price</th>
            <th className='py-2 px-4 border-b'>Deposit</th>
            {/* <th className='py-2 px-4 border-b'>View</th> */}
            <th className='py-2 px-4 border-b'>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data?.map(availableRoomType => (
            <tr
              key={availableRoomType.available_room_type_id}
              className='text-center'
            >
              <td className='py-2 px-4 border-b'>
                {availableRoomType.room_type.room_type_name}
              </td>
              <td className='py-2 px-4 border-b'>
                {availableRoomType.available_room_type_price}
              </td>
              <td className='py-2 px-4 border-b'>
                {availableRoomType.available_room_type_deposit_amount}
              </td>

              {/* <td className='py-2 px-4 border-b'>
              <Button
                variant='primary'
                onClick={() =>
                  onView(
                    availableRoomType.apartment_id,
                    availableRoomType.available_room_type_id,
                  )
                }
              >
                View
              </Button>
            </td> */}

              <td className='py-2 px-4 border-b space-x-2'>
                <Button
                  variant='secondary'
                  onClick={() => onEdit(availableRoomType)}
                >
                  Edit
                </Button>
                <Button
                  variant='danger'
                  onClick={() =>
                    onDelete(
                      availableRoomType.apartment_id,
                      availableRoomType.available_room_type_id,
                    )
                  }
                >
                  Delete
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default AvailableRoomTypeTable
