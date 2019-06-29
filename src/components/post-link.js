/* jshint esversion: 6 */
import React from "react";
import { Link } from "gatsby";

const PostLink = ({ post }) => (
  <>
    <dt>
      <Link to={post.frontmatter.path}>
        {post.frontmatter.title}
      </Link>
    </dt>
    <dd>
      <p>
        {post.excerpt}
      </p>
    </dd>
  </>
)

export default PostLink
