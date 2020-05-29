import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import {BlogListComponent} from "./blogs/blog-list.component";
import {AddBlogomponent} from "./blogs/add-blog.component";

const appRoutes: Routes = [
  // { path: "", redirectTo: "", pathMatch: "full" },
  { path: "", component: BlogListComponent},
  { path: "**", redirectTo: "404", pathMatch: "full" },
  { path: 'add-blog', component: AddBlogomponent },
];

export const appRoutingProviders: any[] = [];

export const routing = RouterModule.forRoot(appRoutes);

//
// const routes: Routes = [
//   { path: "", redirectTo: "/home", pathMatch: "full" }, //default route
//   { path: "home", component: HomeComponent },
//   { path: "about", component: AboutComponent },
//   { path: "contact", component: ContactComponent },
//   { path: "posts", component: PastPostsComponent },
//   { path: "post/:id", component: ViewPostComponent },
//   { path: "author-post", component: AuthorPostComponent }
// ];
