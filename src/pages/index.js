/* jshint esversion: 6 */
import React from "react";
import { graphql } from "gatsby";
import PostLink from "../components/post-link";
import { Link } from "gatsby";
import Layout from "../components/layout";
import SEO from "../components/seo"

const IndexPage = ({
  data: {
    allMarkdownRemark: { edges },
  },
}) => {
  const Posts = edges
    .filter(edge => !!edge.node.frontmatter.date) // You can filter your posts based on some criteria
    .map(edge => <PostLink key={edge.node.id} post={edge.node} />);
  return <Layout>
    <SEO title="Home" />
    <h1>Cultural Guideposts</h1>
    <dl>{Posts}</dl>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
}

export default IndexPage

export const pageQuery = graphql`
  query {
    allMarkdownRemark(sort: { order: DESC, fields: [frontmatter___date] }) {
      edges {
        node {
          id
          excerpt(pruneLength: 250)
          frontmatter {
            date(formatString: "MMMM DD, YYYY")
            path
            title
          }
          wordCount {
            paragraphs
            sentences
            words
          }
        }
      }
    }
  }
`
