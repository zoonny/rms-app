import { lazy } from 'react';

// project import
import Loadable from 'components/Loadable';
import DashboardLayout from 'layout/DashboardLayout';
import PlayPage from 'pages/extra-pages/play-page';
import ExamplePage from 'pages/extra-pages/example-page';
import QRcodePage from 'pages/extra-pages/qrcode-page';
import QRCodeScannerPage from 'pages/extra-pages/qrcode-scanner-page';

const Color = Loadable(lazy(() => import('pages/component-overview/color')));
const Typography = Loadable(lazy(() => import('pages/component-overview/typography')));
const Shadow = Loadable(lazy(() => import('pages/component-overview/shadows')));
const DashboardDefault = Loadable(lazy(() => import('pages/dashboard/index')));

// render - sample page
const SamplePage = Loadable(lazy(() => import('pages/extra-pages/sample-page')));

// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
  path: '/',
  element: <DashboardLayout />,
  children: [
    {
      path: '/',
      element: <DashboardDefault />
    },
    // {
    //   path: 'color',
    //   element: <Color />
    // },
    {
      path: 'dashboard',
      children: [
        {
          path: 'default',
          element: <DashboardDefault />
        }
      ]
    },
    // {
    //   path: 'sample-page',
    //   element: <SamplePage />
    // },
    // {
    //   path: 'play-page',
    //   element: <PlayPage />
    // },
    // {
    //   path: 'example-page',
    //   element: <ExamplePage />
    // },
    // {
    //   path: 'shadow',
    //   element: <Shadow />
    // },
    // {
    //   path: 'typography',
    //   element: <Typography />
    // },
    // {
    //   path: 'qrcode-page',
    //   element: <QRcodePage />
    // },
    // {
    //   path: 'qrcode-scanner-page',
    //   element: <QRCodeScannerPage />
    // }
  ]
};

export default MainRoutes;
