import { Outlet } from 'react-router-dom'
import Sidebar from './layout/Sidebar'

function AdminDashboardIndex() {
  return (
    <div className='flex min-h-screen'>
      <Sidebar />
      <div className='flex-grow p-8 bg-gray-100 min-h-screen'>
        <Outlet />
      </div>
    </div>
  )
}

export default AdminDashboardIndex
