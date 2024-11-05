import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import './index.css'
import 'react-toastify/dist/ReactToastify.css'
import { ToastContainer } from 'react-toastify'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import { red } from '@mui/material/colors' // New Apartment Detail Component
import Index from './routes/Index'
import ErrorPage from './error-page'
import Home from './routes/Home' // New Home Component
import Register from './routes/Register'
import Login from './routes/Login'
import About from './routes/About'
import Contact from './routes/Contact'
import Bookings from './routes/Bookings'
// Admin routes
import AdminIndex from './routes/admin/AdminIndex'
import AdminLogin from './routes/admin/AdminLogin'
import AdminDashboardIndex from './routes/admin/dashboard/AdminDashboardIndex'
import ApartmentRegister from './routes/admin/dashboard/apartment/ApartmentRegister'
import ApartmentList from './routes/admin/dashboard/apartment/ApartmentList'
import ApartmentDetail from './routes/admin/dashboard/apartment/ApartmentDetail'
import AdminHome from './routes/admin/dashboard/AdminHome'
import ApartmentUpdate from './routes/admin/dashboard/apartment/ApartmentUpdate'
import AvailableRoomTypeList from './routes/admin/dashboard/apartment/available_room_types/AvailableRoomTypeList'
import AvailableRoomTypeRegister from './routes/admin/dashboard/apartment/available_room_types/AvailableRoomTypeRegister'
import AvailableRoomTypeUpdate from './routes/admin/dashboard/apartment/available_room_types/AvailableRoomTypeUpdate'
import RoomList from './routes/admin/dashboard/apartment/room/RoomList'
import RoomRegister from './routes/admin/dashboard/apartment/room/RoomRegister'
import RoomUpdate from './routes/admin/dashboard/apartment/room/RoomUpdate'
import RentalRegister from './routes/admin/dashboard/rental/RentalRegister'
import RentalList from './routes/admin/dashboard/rental/RentalList'
// New Client routes
import ApartmentCatalogPage from './routes/ApartmentCatalogPage'
import ApartmentDetailClient from './routes/ApartmentDetailClient'
import theme from '../theme'
import BookingList from './routes/admin/dashboard/booking/BookingList'
import InvoiceList from './routes/admin/dashboard/rental/invoice/InvoiceList'
import InvoiceRegister from './routes/admin/dashboard/rental/invoice/InvoiceRegister'
import InvoiceUpdate from './routes/admin/dashboard/rental/invoice/InvoiceUpdate'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Index />,
    errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        path: '/',
        element: <Home />,
      },
      {
        path: '/Home',
        element: <Home />,
      },
      {
        path: '/contact',
        element: <Contact />,
      },
      {
        path: '/aboutus',
        element: <About />,
      },
      {
        path: '/signup',
        element: <Register />,
      },
      {
        path: '/signin',
        element: <Login />,
      },
      {
        path: '/apartments',
        element: <ApartmentCatalogPage />,
      },
      {
        path: '/apartments/:id',
        element: <ApartmentDetailClient />,
      },
      {
        path: '/bookings',
        element: <Bookings />,
      },
    ],
  },
  {
    path: '/admin',
    element: <AdminIndex />,
    errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        path: '/admin',
        element: <AdminLogin />,
      },
    ],
  },
  {
    path: '/admin/dashboard',
    element: <AdminDashboardIndex />,
    errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        path: '/admin/dashboard',
        element: <ApartmentList />,
      },
      // ------Apartments-----------//
      {
        path: '/admin/dashboard/apartments',
        element: <ApartmentList />,
      },
      {
        path: '/admin/dashboard/apartments/:id',
        element: <ApartmentDetail />,
      },
      {
        path: '/admin/dashboard/apartments/register',
        element: <ApartmentRegister />,
      },
      {
        path: '/admin/dashboard/apartments/:id/update',
        element: <ApartmentUpdate />,
      },
      // ------Available room types-----------//
      {
        path: '/admin/dashboard/apartments/:id/available_room_types',
        element: <AvailableRoomTypeList />,
      },
      {
        path: '/admin/dashboard/apartments/:id/available_room_types/register',
        element: <AvailableRoomTypeRegister />,
      },
      {
        path: '/admin/dashboard/apartments/:id/available_room_types/:available_room_type_id/update',
        element: <AvailableRoomTypeUpdate />,
      },
      // ------ rooms -----------//
      {
        path: '/admin/dashboard/apartments/:id/rooms',
        element: <RoomList />,
      },
      {
        path: '/admin/dashboard/apartments/:id/rooms/register',
        element: <RoomRegister />,
      },
      {
        path: '/admin/dashboard/apartments/:id/rooms/:room_id/update',
        element: <RoomUpdate />,
      },
      // ------ Bookings -----------//
      {
        path: '/admin/dashboard/bookings',
        element: <BookingList />,
      },
      // ------ Rentals -----------//
      {
        path: '/admin/dashboard/rentals',
        element: <RentalList />,
      },
      {
        path: '/admin/dashboard/rentals/register',
        element: <RentalRegister />,
      },
      // ------ Invoices -----------//
      {
        path: '/admin/dashboard/rentals/:rental_id/invoices',
        element: <InvoiceList />,
      },
      {
        path: '/admin/dashboard/rentals/:rental_id/invoices/register',
        element: <InvoiceRegister />,
      },
      {
        path: '/admin/dashboard/rentals/:rental_id/invoices/:invoice_id/update',
        element: <InvoiceUpdate />,
      },
    ],
  },
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ThemeProvider theme={theme}>
      <RouterProvider router={router} />
      <ToastContainer />
    </ThemeProvider>
  </StrictMode>,
)
