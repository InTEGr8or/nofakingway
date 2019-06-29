/* jshint esversion: 6 */

import React from "react";
import PropTypes from "prop-types";
import Helmet from "react-helmet";
import { useStaticQuery, graphql } from "gatsby"

const PodcastAudio = ({ description, lang, meta, keywords, title }) => {
    <audio src="{{ site.siteMetadata.bbURL }}{{ .Params.audio }}" preload="auto" controls></audio>
}
export default podcastAudio;
