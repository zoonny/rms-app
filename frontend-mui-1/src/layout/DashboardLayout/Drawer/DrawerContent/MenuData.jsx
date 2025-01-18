// Define the menu data with 3 levels of depth
// Navigation : Dashboard
// Authentication : Login, Register
// Utilities : Typhography, Color, Shadow

import { HomeOutlined, LoginOutlined, StarOutlined, ToolOutlined } from '@ant-design/icons';

// Support : Sample Page, Play Page, Example Page, Documentation
const menuData = [
  {
    title: '현황',
    path: '',
    icon: <HomeOutlined />,
    depth: 0,
    items: [
      {
        title: '대시보드',
        path: '/',
        icon: null,
        depth: 1,
        items: []
      }
    ]
  },
  // {
  //   title: 'Authentication',
  //   path: '',
  //   icon: <LoginOutlined />,
  //   depth: 0,
  //   items: [
  //     {
  //       title: 'Login',
  //       path: '/login',
  //       icon: null,
  //       depth: 1,
  //       items: []
  //     },
  //     {
  //       title: 'Register',
  //       path: '/register',
  //       icon: null,
  //       depth: 1,
  //       items: []
  //     }
  //   ]
  // },
  // {
  //   title: 'Utilities',
  //   path: '',
  //   icon: <ToolOutlined />,
  //   depth: 0,
  //   items: [
  //     {
  //       title: 'Typography',
  //       path: '/typography',
  //       icon: null,
  //       depth: 1,
  //       items: []
  //     },
  //     {
  //       title: 'Color',
  //       path: '/color',
  //       icon: null,
  //       depth: 1,
  //       items: []
  //     },
  //     {
  //       title: 'Shadow',
  //       path: '/shadow',
  //       icon: null,
  //       depth: 1,
  //       items: []
  //     },
  //     {
  //       title: 'Test',
  //       path: '',
  //       icon: null,
  //       depth: 1,
  //       items: [
  //         {
  //           title: 'Web Development',
  //           path: '',
  //           icon: null,
  //           depth: 2,
  //           items: []
  //         },
  //         {
  //           title: 'Mobile Development',
  //           path: '',
  //           icon: null,
  //           depth: 2,
  //           items: [
  //             {
  //               title: 'iOS',
  //               path: '',
  //               icon: null,
  //               depth: 3,
  //               items: []
  //             },
  //             {
  //               title: 'Android',
  //               path: '',
  //               icon: null,
  //               depth: 3,
  //               items: []
  //             }
  //           ]
  //         }
  //       ]
  //     }
  //   ]
  // },
  // {
  //   title: 'Support',
  //   path: '',
  //   icon: <StarOutlined />,
  //   depth: 0,
  //   items: [
  //     {
  //       title: 'Sample Page',
  //       path: '/sample-page',
  //       icon: null,
  //       depth: 1,
  //       closeable: true,
  //       single: true,
  //       items: []
  //     },
  //     {
  //       title: 'Play Page',
  //       path: '/play-page',
  //       icon: null,
  //       depth: 1,
  //       closeable: true,
  //       single: true,
  //       items: []
  //     },
  //     {
  //       title: 'Example Page',
  //       path: '/example-page',
  //       icon: null,
  //       depth: 1,
  //       closeable: true,
  //       items: []
  //     },
  //     {
  //       title: 'QRCode Page',
  //       path: '/qrcode-page',
  //       icon: null,
  //       depth: 1,
  //       closeable: true,
  //       items: []
  //     },
  //     {
  //       title: 'QRCode Scanner Page',
  //       path: '/qrcode-scanner-page',
  //       icon: null,
  //       depth: 1,
  //       closeable: true,
  //       items: []
  //     },
  //     {
  //       title: 'Documentation',
  //       path: '',
  //       icon: null,
  //       depth: 1,
  //       items: []
  //     }
  //   ]
  // }
];

export default menuData;
