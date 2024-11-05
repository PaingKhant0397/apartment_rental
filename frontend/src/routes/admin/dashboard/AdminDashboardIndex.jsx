import { useEffect, useState } from 'react'
import { Outlet, useNavigate } from 'react-router-dom'
import { AppBar, Toolbar, IconButton, Typography, Button } from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'
import Sidebar from './layout/Sidebar'
import { removeItem, getItem } from '../../../utils/localStorageUtils' // Adjust the path according to your project structure

function AdminDashboardIndex() {
  const [isSidebarOpen, setSidebarOpen] = useState(false)
  const navigate = useNavigate() // Initialize navigate

  const toggleSidebar = () => {
    setSidebarOpen(prev => !prev)
  }

  const handleLogout = () => {
    removeItem('adminToken') // Remove the admin token from local storage
    navigate('/admin/') // Redirect to the login page
  }
  useEffect(() => {
    // Check for adminToken in local storage
    const token = getItem('adminToken')
    if (!token) {
      navigate('/admin') // Redirect to homepage if token is not found
    }
  }, [navigate])

  return (
    <div className='flex min-h-screen'>
      <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />
      <div className='flex-grow'>
        <AppBar position='fixed'>
          <Toolbar>
            <IconButton
              edge='start'
              color='inherit'
              aria-label='menu'
              onClick={toggleSidebar}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant='h6' style={{ flexGrow: 1 }}>
              Admin Dashboard
            </Typography>
            <Button color='inherit' onClick={handleLogout}>
              Logout
            </Button>
          </Toolbar>
        </AppBar>
        <div className='p-8 bg-gray-100 min-h-screen pt-20'>
          {' '}
          {/* Increased pt from 16 to 20 */}
          <Outlet />
        </div>
      </div>
    </div>
  )
}

export default AdminDashboardIndex
