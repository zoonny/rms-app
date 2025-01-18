// project import
import NavCard from './NavCard';
import Navigation from './Navigation';
import SimpleBar from 'components/third-party/SimpleBar';
import NavigationTree from './NavigationTree';
import NavigationMenu from './NavigationMenu';

// ==============================|| DRAWER CONTENT ||============================== //

export default function DrawerContent() {
  return (
    <>
      <SimpleBar sx={{ '& .simplebar-content': { display: 'flex', flexDirection: 'column' } }}>
        <NavigationMenu />
        {/* <NavigationTree /> */}
        {/* <Navigation /> */}
        {/* <NavCard /> */}
      </SimpleBar>
    </>
  );
}
