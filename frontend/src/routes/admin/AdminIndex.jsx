import { Outlet } from 'react-router-dom'
// import Header from './layout/Header'
// import Footer from './layout/Footer'

export default function AdminIndex() {
  return (
    <>
      {/* <Header /> */}
      <main>
        <Outlet />
      </main>
      {/* <Footer /> */}
    </>
  )
}
