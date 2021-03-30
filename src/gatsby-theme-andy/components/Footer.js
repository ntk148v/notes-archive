/** @jsx jsx */
import { Styled, jsx, Box } from 'theme-ui';

import ReferredBlock from 'gatsby-theme-andy/src/components/ReferredBlock.js';

const Footer = ({ references }) => {
  return (
    <Box p={3} sx={{ borderRadius: 2 }} mb={2} bg="accent" color="text-light">
      <ReferredBlock references={references} />
      <p sx={{ m: 0, fontSize: 1 }}>
        If you think this note resonated, be it positive or negative, please feel free to send me an{' '}
        <Styled.a sx={{ textDecoration: 'underline', color: 'text-light' }} href="mailto:kiennt2609@gmail.com">
          email
        </Styled.a>{' '}
        and we can talk.
      </p>
    </Box>
  );
};

export default Footer;
