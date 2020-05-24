import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

const appRoutes: Routes = [
  { path: "", redirectTo: "", pathMatch: "full" },
  { path: "**", redirectTo: "404", pathMatch: "full" },
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
