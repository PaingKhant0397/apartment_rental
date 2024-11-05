import { Drawer, List, ListItem, ListItemText, IconButton } from '@mui/material'
import { NavLink } from 'react-router-dom'
import MenuIcon from '@mui/icons-material/Menu'
import CloseIcon from '@mui/icons-material/Close'

export default function Sidebar({ isOpen, toggleSidebar }) {
  const navLinkList = [
    { name: 'Home', to: '/admin/dashboard' },
    { name: 'Apartment Register', to: '/admin/dashboard/apartments/register' },
    { name: 'Apartment List', to: '/admin/dashboard/apartments/' },
    { name: 'Booking List', to: '/admin/dashboard/bookings' },
    { name: 'Rental List', to: '/admin/dashboard/rentals' },
  ]

  return (
    <Drawer
      anchor='left'
      open={isOpen}
      onClose={toggleSidebar}
      variant='temporary' // Use 'temporary' for mobile responsiveness
    >
      <div style={{ width: 250 }}>
        <IconButton onClick={toggleSidebar}>
          <CloseIcon />
        </IconButton>
        <List>
          {navLinkList.map((navLink, index) => (
            <ListItem
              button
              component={NavLink}
              to={navLink.to}
              key={index}
              onClick={toggleSidebar}
            >
              <ListItemText primary={navLink.name} />
            </ListItem>
          ))}
        </List>
      </div>
    </Drawer>
  )
}
