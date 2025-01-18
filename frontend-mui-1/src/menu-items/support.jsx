// assets
import { ChromeOutlined, QuestionOutlined } from '@ant-design/icons';
import { QrCode2Outlined } from '@mui/icons-material';

// icons
const icons = {
  ChromeOutlined,
  QuestionOutlined,
  QrCode2Outlined
};

// ==============================|| MENU ITEMS - SAMPLE PAGE & DOCUMENTATION ||============================== //

const support = {
  id: 'support',
  title: 'Support',
  type: 'group',
  children: [
    {
      id: 'sample-page',
      title: 'Sample Page',
      type: 'item',
      url: '/sample-page',
      icon: ChromeOutlined
    },
    {
      id: 'play-page',
      title: 'Play Page',
      // type: 'collapse',
      // group, collapse, item
      type: 'item',
      url: '/play-page',
      icon: icons.ChromeOutlined
      // children: [
      //   {
      //     id: 'play-page',
      //     title: 'Play Page',
      //     type: 'item',
      //     url: '/play-page',
      //     icon: icons.ChromeOutlined
      //   }
      // ]
    },
    {
      id: 'example-page',
      title: 'Example Page',
      type: 'item',
      url: '/example-page',
      icon: icons.ChromeOutlined
    },
    {
      id: 'qrcode-page',
      title: 'QRCode Page',
      type: 'item',
      url: '/qrcode-page',
      icon: icons.QrCode2Outlined
    },
    {
      id: 'documentation',
      title: 'Documentation',
      type: 'item',
      url: 'https://codedthemes.gitbook.io/mantis/',
      icon: icons.QuestionOutlined,
      external: true,
      target: true
    }
  ]
};

export default support;
