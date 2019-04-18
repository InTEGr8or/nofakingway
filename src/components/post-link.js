import React from "react"
import { Link } from "gatsby"

const PostLink = ({ post }) => (
  <li>
    <Link to={post.frontmatter.path}>
      {post.frontmatter.title}
    </Link>
    <p>
      {post.excerpt}
    </p>
  </li>
)

export default PostLink
